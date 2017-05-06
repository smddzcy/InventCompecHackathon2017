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
