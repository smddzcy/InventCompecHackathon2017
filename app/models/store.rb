class Store < ApplicationRecord
  belongs_to :city
  has_many :inventory_position
end
