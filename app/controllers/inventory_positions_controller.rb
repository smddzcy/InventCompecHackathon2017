class InventoryPositionsController < ApplicationController
  before_action :set_inventory_position, only: [:show, :update, :destroy]

  # GET /inventory_positions
  api :GET, '/inventory_positions', 'Retrieves all inventory positions'
  def index
    @inventory_positions = InventoryPosition.all

    paginate json: @inventory_positions, per_page: 100
  end

  # GET /inventory_positions/1
  api :GET, '/inventory_positions/:id', 'Retrieves an inventory position with the given id'
  param :id, :number
  def show
    render json: @inventory_position
  end

  # POST /inventory_positions
  api :POST, '/inventory_positions', 'Creates an inventory position'
  param :store_id, :number
  param :product_id, :number
  param :sales_quantity, :number
  param :store_stock, :number
  param :incoming_stock, :number
  param :sales_revenue, :number
  param :date, String
  def create
    @inventory_position = InventoryPosition.new(inventory_position_params)

    if @inventory_position.save
      render json: @inventory_position, status: :created, location: @inventory_position
    else
      render json: @inventory_position.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /inventory_positions/1
  api :PUT, '/inventory_positions/:id', 'Updates an inventory position'
  param :id, :number
  param :store_id, :number
  param :product_id, :number
  param :sales_quantity, :number
  param :store_stock, :number
  param :incoming_stock, :number
  param :sales_revenue, :number
  param :date, String
  def update
    if @inventory_position.update(inventory_position_params)
      render json: @inventory_position
    else
      render json: @inventory_position.errors, status: :unprocessable_entity
    end
  end

  # DELETE /inventory_positions/1
  api :DELETE, '/inventory_positions/:id', 'Deletes an inventory position'
  param :id, :number
  def destroy
    @inventory_position.destroy
  end

  # GET /inventory_positions/sales_quantity
  api :GET, '/inventory_positions/sales_quantity', 'Gives the daily sales quantity for the given time period and product group'
  example '[
    {
      "date": "2016-01-01",
      "sales_quantity": 182
    },
    {
      "date": "2016-01-02",
      "sales_quantity": 222
    },
    {
      "date": "2016-01-03",
      "sales_quantity": 219
    },
    {
      "date": "2016-01-04",
      "sales_quantity": 77
    }
  ]'
  param :start_date, String
  param :end_date, String
  param :product_group, :number
  param :product_id, :number, "Optional, if product_id is given, product_group will be unused"
  def sales_quantity
    start_date = params[:start_date].to_date()
    end_date = params[:end_date].to_date()
    product_group = params[:product_group]
    product_id = params[:product_id]

    result = InventoryPosition.joins(:product).where(date: start_date..end_date)

    if product_id.present?
      result = result.where(products: {id: product_id})
    else
      result = result.where(products: {product_group: product_group})
    end

    result = result.all.group_by(&:date).map do |k, el|
      { date: k, sales_quantity: el.map(&:sales_quantity).sum }
    end

    render json: result
  end

  # GET /inventory_positions/predict_sales_quantity
  api :GET, '/inventory_positions/predict_sales_quantity', 'Gives the daily sales quantity predictions for the given parameters'
  example '[
    {
      "date": "2017-01-01",
      "predict_sales_quantity": 1.0319905281066895
    },
    {
      "date": "2017-01-02",
      "predict_sales_quantity": 1.0339000225067139
    },
    {
      "date": "2017-01-03",
      "predict_sales_quantity": 1.0358095169067383
    },
    {
      "date": "2017-01-04",
      "predict_sales_quantity": 1.0377191305160522
    }
  ]'
  param :start_date, String
  param :end_date, String
  param :store_id, :number
  param :product_id, :number
  param :price, String
  def predict_sales_quantity
    start_date = params[:start_date].to_date()
    end_date = params[:end_date].to_date()
    store_id = params[:store_id]
    product_id = params[:product_id]
    price = params[:price]

    # Build the prediction input.
    predict_in = []
    (start_date.to_date..end_date.to_date).to_a.each_with_index do |date, i|
      predict_in << [date.day, date.month, "#{date.day}#{"%02d" % date.month}".to_i,
                     store_id, product_id, price]
    end
    predict_in = JSON.generate(predict_in).gsub('"', '')

    # Get the prediction output from prediction script, which uses the trained
    # TensorFlow model.
    predict_out = `python #{Rails.root.to_s}/tensorflow-ml/predict.py "#{predict_in}"`
    predict_out = JSON.parse(predict_out)

    # Build the result json array.
    result = []
    (start_date.to_date..end_date.to_date).to_a.each_with_index do |date, i|
      result << {
        date: date,
        predict_sales_quantity: predict_out[i][0]
      }
    end

    render json: result
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_inventory_position
      @inventory_position = InventoryPosition.find(params[:id])
    end

    # Only allow a trusted parameter "white list" through.
    def inventory_position_params
      params.require(:inventory_position).permit(:store_id, :product_id,
          :sales_quantity, :store_stock, :incoming_stock, :sales_revenue, :date)
    end
end
