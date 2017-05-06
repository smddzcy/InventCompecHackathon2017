require "rails_helper"

RSpec.describe InventoryPositionsController, type: :routing do
  describe "routing" do

    it "routes to #index" do
      expect(:get => "/inventory_positions").to route_to("inventory_positions#index")
    end

    it "routes to #new" do
      expect(:get => "/inventory_positions/new").to route_to("inventory_positions#new")
    end

    it "routes to #show" do
      expect(:get => "/inventory_positions/1").to route_to("inventory_positions#show", :id => "1")
    end

    it "routes to #edit" do
      expect(:get => "/inventory_positions/1/edit").to route_to("inventory_positions#edit", :id => "1")
    end

    it "routes to #create" do
      expect(:post => "/inventory_positions").to route_to("inventory_positions#create")
    end

    it "routes to #update via PUT" do
      expect(:put => "/inventory_positions/1").to route_to("inventory_positions#update", :id => "1")
    end

    it "routes to #update via PATCH" do
      expect(:patch => "/inventory_positions/1").to route_to("inventory_positions#update", :id => "1")
    end

    it "routes to #destroy" do
      expect(:delete => "/inventory_positions/1").to route_to("inventory_positions#destroy", :id => "1")
    end

  end
end
