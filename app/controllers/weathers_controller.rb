class WeathersController < ApplicationController
  before_action :set_weather, only: [:show, :update, :destroy]

  # GET /weathers
  api :GET, "/weathers", "Retrieves all weather info"
  def index
    @weathers = Weather.all

    render json: @weathers
  end

  # GET /weathers/1
  api :GET, "/weathers/:id", "Retrieves a weather info with the given id"
  param :id, :number, "ID of the weather info"
  def show
    render json: @weather
  end

  # POST /weathers
  api :POST, "/weathers", "Creates a weather info"
  param :city_id, :number, "City ID of the weather info"
  param :date, String, "Date of the weather info"
  param :temperature, String, "Temperature value"
  param :type, String, "Type of the weather, ex: Clouds, Rainy, Windy, Sunny"
  def create
    @weather = Weather.new(weather_params)

    if @weather.save
      render json: @weather, status: :created, location: @weather
    else
      render json: @weather.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /weathers/1
  api :PUT, "/weathers/:id", "Updates a weather info"
  param :id, :number, "ID of the weather info"
  param :city_id, :number, "City ID of the weather info"
  param :date, String, "Date of the weather info"
  param :temperature, String, "Temperature value"
  param :type, String, "Type of the weather, ex: Clouds, Rainy, Windy, Sunny"
  def update
    if @weather.update(weather_params)
      render json: @weather
    else
      render json: @weather.errors, status: :unprocessable_entity
    end
  end

  # DELETE /weathers/1
  api :DELETE, "/weathers/:id", "Deletes a weather info"
  param :id, :number, "ID of the weather info"
  def destroy
    @weather.destroy
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_weather
      @weather = Weather.find(params[:id])
    end

    # Only allow a trusted parameter "white list" through.
    def weather_params
      params.require(:weather).permit(:city_id, :date, :temperature, :type)
    end
end
