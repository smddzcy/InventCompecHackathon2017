require "net/http"
require "uri"

namespace :api do
  desc "Gets the weather data from OpenWeatherMap API and fills it to the Weather table"
  task get_weather_data: :environment do
  end
end
