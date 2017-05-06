# == Schema Information
#
# Table name: cities
#
#  id        :integer          not null, primary key
#  name      :string
#  latitude  :float
#  longitude :float
#

class City < ApplicationRecord
  acts_as_copy_target
  has_many :store
  has_many :weather
end
