class CreateInventoryPositions < ActiveRecord::Migration[5.0]
  def change
    create_table :inventory_positions do |t|
      t.references :store, foreign_key: true
      t.references :product, foreign_key: true
      t.integer :sales_quantity
      t.integer :store_stock
      t.integer :incoming_stock
      t.float :sales_revenue
      t.date :date

      t.timestamps
    end
  end
end
