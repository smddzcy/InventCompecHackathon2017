Rails.application.routes.draw do
  resources :products
  resources :inventory_positions
  resources :stores
  resources :cities
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
