# == Schema Information
#
# Table name: products
#
#  id            :integer          not null, primary key
#  product_group :integer
#  price         :float
#  cost          :float
#

FactoryGirl.define do
  factory :product do
    product_group 1
    price 1.5
    cost 1.5
  end
end
