Rails.application.routes.draw do
  apipie

  get "inventory_positions/sales_quantity" => "inventory_positions#sales_quantity"
  get "inventory_positions/predict_sales_quantity" => "inventory_positions#predict_sales_quantity"

  resources :weathers
  resources :products
  resources :inventory_positions
  resources :stores
  resources :cities
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
