# Django Auction Project

This Django project implements an auction website where users can list items for bidding, place bids, and interact with other users through comments and wishlists.

## Features

- **User Authentication**: Users can register, log in, and log out.
- **Lot Management**: Users can create, view, and close lots for bidding.
- **Bidding System**: Users can place bids on open lots, with the highest bid and bidder dynamically updated.
- **Category Management**: Lots are categorized under main and sub-categories.
- **Comments**: Users can leave comments on lots.
- **Wishlist**: Users can bookmark lots to their wishlist.
- **Pagination**: Paginated listing of lots across different categories.

## Technologies Used

- **Python**: Backend development using Django.
- **Django**: Python web framework for building web applications.
- **Bootstrap 5**: Frontend styling and components.
- **SQLite**: Default database engine provided by Django.

## Installation

- Install python 3.x
- Intstall required packages

        pip3 install -r requirements.txt

### Run server

    python3 manage.py runserver

- Open your web browser and go to http://127.0.0.1:8000/
