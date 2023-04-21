# Api_restaurant

## Feauters:
- JWT authentication
- Admin panel at /admin/
- Login by email
- Rating restaurant menu 
- Filtering menu for current day
- Auto clearing votes (Celery)
- Creating menu for special day
- Getting restaurnt winner 

## Endpoints sense:

### USER :

- [POST] /api/user/registration/   (register your user) !
- [POST] /api/user/token/   (get your JWT token for access) !
- [GET] /api/user/me   (info about yourself)
- [PUT] /api/user/me   (update all info about yourself)
- [PATCH] /api/user/me  (partial update of info about yourself)
- [POST] /api/user/token/refresh (update your access token)

### MENU :

- [POST] /api/menu/    (create nem menu and add it to exiting restourant) !
- [GET] /api/menu/   (list of all menu)
- [GET] /api/menu/{id}   (detail info about menu)
- [PUT] /api/menu/{id} {id}   (update all menu instance)
- [PATCH] /api/menu/{id}   (partial update of menu instance)
- [DELETE] /api/menu/{id}   (delete menu with chosen id)
- [GET] /api/menu/choose_place_for_today/ (list of all menu filter by currenr week day) !
- [GET] /api/menu/today_results/  ( get resourant and menu with won by votes ) ! 

### RESTAURNAT :

- [GET] /api/restaurants/   (list of all restaurants) !
- [POST] /api/restaurants/   (create restaurant) !
- [GET] /api/restaurants/{id}   (detail info about restaurant)
- [PUT] /api/restaurants/{id}   (update all borrow restaurants)
- [PATCH] /api/restaurants/{id}   (partial update of restaurants instance)
- [DELETE] /api/restaurants/{id}   (delete borrow with chosen id)

## Installing using GitHub:
```python
git clone https://github.com/DevSpaciX/Api_restaurant.git
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
docker-compose up
```
## Getting access:
- Create user via /api/user/registration/
- Admin user credetnials : admin@admin.com / pass : 123123 
- Get user token via /api/user/token/
- Install ModHeader extention and create Request header with value ```Bearer <Your access tokekn>```
![image](https://user-images.githubusercontent.com/102595649/233555996-e65eb31a-dd26-4cac-b7c4-b2b5a20d4672.png)


## Screenshots:
![image](https://user-images.githubusercontent.com/102595649/233555826-091dd115-a052-45ab-9293-919a52b4ad94.png)
![image](https://user-images.githubusercontent.com/102595649/233555844-efb59d30-46e1-4ecd-aba7-5421c88a3b11.png)
![image](https://user-images.githubusercontent.com/102595649/233555860-2a92e173-5a37-4115-8e39-0b63d2904b16.png)
![image](https://user-images.githubusercontent.com/102595649/233555890-2c8d4749-3153-4b7d-8235-b7caa22a2cb8.png)
![image](https://user-images.githubusercontent.com/102595649/233555902-b895eaa3-8bea-4e86-9c3b-abab3ba88989.png)
