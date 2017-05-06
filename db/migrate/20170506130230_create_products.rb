class CreateProducts < ActiveRecord::Migration[5.0]
  def change
    create_table :products do |t|
      t.integer :product_group
      t.float :price
      t.float :cost

      t.timestamps
    end
  end
end
