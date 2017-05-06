class ChangeTypeOfDateFieldInInventoryPositions < ActiveRecord::Migration[5.0]
  def change
    execute "set datestyle to SQL,DMY;"
    change_column :inventory_positions, :date, 'date USING date::date'
  end
end
