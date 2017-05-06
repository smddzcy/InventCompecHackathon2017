# == Schema Information
#
# Table name: stores
#
#  id      :integer          not null, primary key
#  city_id :integer
#

FactoryGirl.define do
  factory :store do
    city nil
  end
end
