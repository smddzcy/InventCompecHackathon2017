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
  def sales_quantity
    start_date = params[:start_date].to_date()
    end_date = params[:end_date].to_date()
    product_group = params[:product_group]

    unless start_date and end_date and product_group
      render json: "You should give all the necessary query params", status: :unprocessable_entity
    end

    result = InventoryPosition.joins(:product)
                .where(products: {product_group: product_group})
                .where(date: start_date..end_date)
                .all.group_by(&:date)

    result = result.map do |k, el|
              { date: k, sales_quantity: el.map(&:sales_quantity).sum }
             end

    render json: result
  end

  def predict_sales_quantity
    start_date = params[:start_date].to_date()
    end_date = params[:end_date].to_date()
    product_group = params[:product_group]

    
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
