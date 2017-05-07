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

FactoryGirl.define do
  factory :weather do
    city nil
    date "2017-05-06 18:46:45"
    temperature 1.5
    type ""
  end
end
