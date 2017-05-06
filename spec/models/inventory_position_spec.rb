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
#  date           :string
#

require 'rails_helper'

RSpec.describe InventoryPosition, type: :model do
  pending "add some examples to (or delete) #{__FILE__}"
end
