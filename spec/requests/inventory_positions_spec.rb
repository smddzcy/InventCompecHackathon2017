require 'rails_helper'

RSpec.describe "InventoryPositions", type: :request do
  describe "GET /inventory_positions" do
    it "works! (now write some real specs)" do
      get inventory_positions_path
      expect(response).to have_http_status(200)
    end
  end
end
