# == Schema Information
#
# Table name: weathers
#
#  id          :integer          not null, primary key
#  city_id     :integer
#  date        :datetime
#  temperature :float
#  type        :integer
#  created_at  :datetime         not null
#  updated_at  :datetime         not null
#

class Weather < ApplicationRecord
  belongs_to :city
end
