class CreateWeathers < ActiveRecord::Migration[5.0]
  def change
    create_table :weathers do |t|
      t.references :city, foreign_key: true
      t.datetime :date
      t.float :temperature
      t.integer :type

      t.timestamps
    end
  end
end
