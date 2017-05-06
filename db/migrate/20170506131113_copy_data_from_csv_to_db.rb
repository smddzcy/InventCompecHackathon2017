class CopyDataFromCsvToDb < ActiveRecord::Migration[5.0]
  def change
    City.copy_from "#{Rails.root.to_s}/model_csv_data/city.csv"
    Store.copy_from "#{Rails.root.to_s}/model_csv_data/store.csv"
    Product.copy_from "#{Rails.root.to_s}/model_csv_data/product.csv"
    InventoryPosition.copy_from "#{Rails.root.to_s}/model_csv_data/inventory_position.csv"
  end
end
