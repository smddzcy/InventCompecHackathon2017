class InventoryPositionsController < ApplicationController
  before_action :set_inventory_position, only: [:show, :update, :destroy]

  # GET /inventory_positions
  def index
    @inventory_positions = InventoryPosition.all

    paginate json: @inventory_positions, per_page: 100
  end

  # GET /inventory_positions/1
  def show
    render json: @inventory_position
  end

  # POST /inventory_positions
  def create
    @inventory_position = InventoryPosition.new(inventory_position_params)

    if @inventory_position.save
      render json: @inventory_position, status: :created, location: @inventory_position
    else
      render json: @inventory_position.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /inventory_positions/1
  def update
    if @inventory_position.update(inventory_position_params)
      render json: @inventory_position
    else
      render json: @inventory_position.errors, status: :unprocessable_entity
    end
  end

  # DELETE /inventory_positions/1
  def destroy
    @inventory_position.destroy
  end

  # GET /inventory_positions/sales_quantity?start_date=15.06.2015&end_date=15.09.2017&product_group=5
  def sales_quantity
    start_date = params[:start_date]
    end_date = params[:end_date]
    product_group = params[:product_group]

    InventoryPosition.where()

    render json: sales_quantity
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
