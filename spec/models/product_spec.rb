# == Schema Information
#
# Table name: products
#
#  id            :integer          not null, primary key
#  product_group :integer
#  price         :float
#  cost          :float
#

require 'rails_helper'

RSpec.describe Product, type: :model do
  pending "add some examples to (or delete) #{__FILE__}"
end
