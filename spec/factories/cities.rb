# == Schema Information
#
# Table name: cities
#
#  id        :integer          not null, primary key
#  name      :string
#  latitude  :float
#  longitude :float
#

FactoryGirl.define do
  factory :city do
    name "MyString"
    latitude 1.5
    longitude 1.5
  end
end
