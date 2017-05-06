class InventoryPositionsController < ApplicationController
  before_action :set_inventory_position, only: [:show, :update, :destroy]

  # GET /inventory_positions
  def index
    @inventory_positions = InventoryPosition.all

    render json: @inventory_positions
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
