# == Schema Information
#
# Table name: products
#
#  id            :integer          not null, primary key
#  product_group :integer
#  price         :float
#  cost          :float
#

class Product < ApplicationRecord
  acts_as_copy_target
  has_many :inventory_position
end
