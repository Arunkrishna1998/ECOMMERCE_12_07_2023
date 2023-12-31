from django.urls import path,include

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.index, name="index"),
	path('index', views.index, name="index"),
	path('category_list/', views.category_list, name="category_list"),
	#
	# path('update_item/', views.updateItem, name="update_item"),
	# path('process_order/', views.processOrder, name="process_order"),

	path('login/', views.signin, name="login"),
	path('signin/', views.signin_confirmation, name="signin"),
	path('register/', views.register, name="register"),
	path('validateOTP', views.validateOTP, name="validateOTP"),
	path('customer_logout', views.customer_logout, name="customer_logout"),


	path('admin_login/', views.admin_login, name="admin_login"),
	path('admin_home/', views.admin_home, name="admin_home"),
	path('admin_logout/', views.admin_logout, name="admin_logout"),

	path('admin_user_details_view/', views.admin_user_details_view, name="admin_user_details_view"),
	path('admin_block_unblock/', views.admin_block_unblock, name="admin_block_unblock"),

	path('categories/', views.categories, name="categories"),
	path('admin_categories_add/', views.admin_categories_add, name="admin_categories_add"),
	path('admin_categories_edit', views.admin_categories_edit, name="admin_categories_edit"),
	path('admin_categories_delete', views.admin_categories_delete, name="admin_categories_delete"),

	path('admin_products_view', views.admin_products_view, name="admin_products_view"),
	path('admin_product_add', views.admin_product_add, name="admin_product_add"),
	path('admin_product_update', views.admin_product_update, name="admin_product_update"),

	path('admin_product_details_update', views.admin_product_details_update, name="admin_product_details_update"),
	path('product_variants_view', views.product_variants_view, name="product_variants_view"),
	path('product_variants_add', views.product_variants_add, name="product_variants_add"),
	path('product_variant_images/<uuid:color>/', views.product_variant_images, name='product_variant_images'),
	path('product_variant_images_add', views.product_variant_images_add, name="product_variant_images_add"),
	path('product_image_delete/<uuid:image_id>/<uuid:color>/', views.product_image_delete, name='product_image_delete'),
	# path('products/<int:product_id>/', views.product_details, name='product-details'),
	path('delete_product/', views.delete_product, name='delete_product'),

	path('add_remove_product_to_store/<uuid:product_id>/', views.add_remove_product_to_store, name='add_remove_product_to_store'),
	path('product_variants_stock_update/<uuid:size_id>/<uuid:product_id>/', views.product_variants_stock_update,
		 name='product_variants_stock_update'),
	path('product_variants_stock_updates', views.product_variants_stock_updates,
		 name='product_variants_stock_updates'),

	path('variants_stock_update_cancel/<uuid:product_id>/', views.variants_stock_update_cancel,
		 name='variants_stock_update_cancel'),

	path('admin_order_details_view/', views.admin_order_details_view, name='admin_order_details_view'),
	path('admin_order_info_view/<order>/', views.admin_order_info_view, name='admin_order_info_view'),

	path('order_status_update', views.order_status_update, name='order_status_update'),

	path('product_details/<uuid:product_id>/', views.product_details, name='product_details'),
	path('search_product/', views.search_product, name='search_product'),
	path('search_product_price/', views.search_product_price, name='search_product_price'),

	path('size_list', views.size_list, name='size_list'),
	path('show_price', views.show_price, name='show_price'),

	path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
	path('add_to_cart_1', views.add_to_cart_1, name='add_to_cart_1'),
	path('remove_from_cart_1', views.remove_from_cart_1, name='remove_from_cart_1'),
	path('remove_from_cart', views.remove_from_cart, name='remove_from_cart'),

	path('cart/', views.cart, name="cart"),
	path('view_store/', views.view_store, name="view_store"),
	path('view_store/<slug:category>/', views.view_store, name="view_store_category"),

	path('user_dashboard/', views.user_dashboard, name="user_dashboard"),
	path('checkout/', views.checkout, name="checkout"),
	path('load_address/', views.load_address, name="load_address"),



	path('place_order/', views.place_order, name="place_order"),
	path('payments/<orderno>', views.payments, name="payments"),
	path('order_complete/', views.order_complete, name="order_complete"),
	path('confirm_payments/', views.confirm_payments, name="confirm_payments"),

	path('order_details/<orderno>/', views.order_details, name="order_details"),
	path('cancel_order/<orderno>/', views.cancel_order, name="cancel_order"),

	path('admin_change_password/', views.admin_change_password, name="admin_change_password"),
	path('get_link/', views.get_link, name="get_link"),

	path('admin_coupons_add/', views.admin_coupons_add, name="admin_coupons_add"),
	path('admin_coupons_view/', views.admin_coupons_view, name="admin_coupons_view"),
	path('admin_coupons_update/', views.admin_coupons_update, name="admin_coupons_update"),
	path('admin_coupons_delete/', views.admin_coupons_delete, name="admin_coupons_delete"),

	path('payment/', views.paypal_request, name="payment"),

	path('apply_coupon/', views.apply_coupon, name="apply_coupon"),

	path('user_settings/', views.user_settings, name="user_settings"),
	path('user_profile_view/', views.user_profile_view, name="user_profile_view"),
	path('user_profile_edit/', views.user_profile_edit, name="user_profile_edit"),

	path('user_address_view/', views.user_address_view, name="user_address_view"),
	path('user_address_add/', views.user_address_add, name="user_address_add"),
	path('user_address_edit/', views.user_address_edit, name="user_address_edit"),
	path('user_address_delete/', views.user_address_delete, name="user_address_delete"),
	path('select_address/<int:address_id>/', views.select_address, name="select_address"),



	path('add_item_to_wish_list/<uuid:product_id>/', views.add_item_to_wish_list, name="add_item_to_wish_list"),
	path('remove_item_from_wish_list', views.remove_item_from_wish_list, name="remove_item_from_wish_list"),
	path('user_wish_list_view/', views.user_wish_list_view, name="user_wish_list_view"),

	path('user_view_transaction_details/', views.user_view_transaction_details, name="user_view_transaction_details"),

]