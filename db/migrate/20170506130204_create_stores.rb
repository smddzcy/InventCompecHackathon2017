class CreateStores < ActiveRecord::Migration[5.0]
  def change
    create_table :stores do |t|
      t.references :city, foreign_key: true

      t.timestamps
    end
  end
end
