Apipie.configure do |config|
  config.app_name                = "Wow Analytics"
  config.api_base_url            = ""
  config.doc_base_url            = "/doc"
  config.api_controllers_matcher = "#{Rails.root}/app/controllers/**/*.rb"
  config.app_info                = "Backend API for the Wow Analytics."
end
