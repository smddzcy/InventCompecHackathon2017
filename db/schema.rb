# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 20170506154645) do

  # These are extensions that must be enabled in order to support this database
  enable_extension "plpgsql"

  create_table "cities", force: :cascade do |t|
    t.string "name"
    t.float  "latitude"
    t.float  "longitude"
  end

  create_table "inventory_positions", force: :cascade do |t|
    t.integer "store_id"
    t.integer "product_id"
    t.integer "sales_quantity"
    t.integer "store_stock"
    t.integer "incoming_stock"
    t.float   "sales_revenue"
    t.string  "date"
    t.index ["product_id"], name: "index_inventory_positions_on_product_id", using: :btree
    t.index ["store_id"], name: "index_inventory_positions_on_store_id", using: :btree
  end

  create_table "products", force: :cascade do |t|
    t.integer "product_group"
    t.float   "price"
    t.float   "cost"
  end

  create_table "stores", force: :cascade do |t|
    t.integer "city_id"
    t.index ["city_id"], name: "index_stores_on_city_id", using: :btree
  end

  create_table "weathers", force: :cascade do |t|
    t.integer  "city_id"
    t.datetime "date"
    t.float    "temperature"
    t.integer  "type"
    t.datetime "created_at",  null: false
    t.datetime "updated_at",  null: false
    t.index ["city_id"], name: "index_weathers_on_city_id", using: :btree
  end

  add_foreign_key "inventory_positions", "products"
  add_foreign_key "inventory_positions", "stores"
  add_foreign_key "stores", "cities"
  add_foreign_key "weathers", "cities"
end
