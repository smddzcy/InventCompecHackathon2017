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

require 'rails_helper'

RSpec.describe Weather, type: :model do
  pending "add some examples to (or delete) #{__FILE__}"
end
