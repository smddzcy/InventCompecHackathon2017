# == Schema Information
#
# Table name: inventory_positions
#
#  id             :integer          not null, primary key
#  store_id       :integer
#  product_id     :integer
#  sales_quantity :integer
#  store_stock    :integer
#  incoming_stock :integer
#  sales_revenue  :float
#  date           :date
#

FactoryGirl.define do
  factory :inventory_position do
    store nil
    product nil
    sales_quantity 1
    store_stock 1
    incoming_stock 1
    sales_revenue 1.5
    date "2017-05-06"
  end
end
