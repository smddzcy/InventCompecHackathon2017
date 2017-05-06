# == Schema Information
#
# Table name: stores
#
#  id      :integer          not null, primary key
#  city_id :integer
#

class Store < ApplicationRecord
  acts_as_copy_target
  belongs_to :city
  has_many :inventory_position
end
