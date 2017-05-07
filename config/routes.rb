Rails.application.routes.draw do
  apipie

  get "inventory_positions/sales_quantity" => "inventory_positions#sales_quantity"
  get "inventory_positions/sales_quantity_by_store" => "inventory_positions#sales_quantity_by_store"
  get "inventory_positions/sales_quantity_by_store_by_product" => "inventory_positions#sales_quantity_by_store_by_product"
  get "inventory_positions/predict_sales_quantity" => "inventory_positions#predict_sales_quantity"

  resources :weathers
  resources :products
  resources :inventory_positions
  resources :stores
  resources :cities
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
