class CreateStores < ActiveRecord::Migration[5.0]
  def change
    create_table :stores do |t|
      t.references :city, foreign_key: true
    end
  end
end
