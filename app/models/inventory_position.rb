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

class InventoryPosition < ApplicationRecord
  acts_as_copy_target
  belongs_to :store
  belongs_to :product

  def as_json(options = {})
    super.merge(date: date.strftime('%d.%m.%Y'))
  end
end
