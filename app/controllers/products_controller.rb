class ProductsController < ApplicationController
  before_action :set_product, only: [:show, :update, :destroy]

  # GET /products
  api :GET, "/products", "Retrieves all products"
  def index
    @products = Product.all

    render json: @products
  end

  # GET /products/1
  api :GET, "/products/:id", "Retrieves a product with the given id"
  param :id, :number
  def show
    render json: @product
  end

  # POST /products
  api :POST, "/products", "Creates a product"
  param :product_group, :number
  param :price, String
  param :cost, String
  def create
    @product = Product.new(product_params)

    if @product.save
      render json: @product, status: :created, location: @product
    else
      render json: @product.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /products/1
  api :PUT, "/products/:id", "Updates a product"
  param :id, :number
  param :product_group, :number
  param :price, String
  param :cost, String
  def update
    if @product.update(product_params)
      render json: @product
    else
      render json: @product.errors, status: :unprocessable_entity
    end
  end

  # DELETE /products/1
  api :DELETE, "/products/:id", "Deletes a product"
  param :id, :number
  def destroy
    @product.destroy
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_product
      @product = Product.find(params[:id])
    end

    # Only allow a trusted parameter "white list" through.
    def product_params
      params.require(:product).permit(:product_group, :price, :cost)
    end
end
