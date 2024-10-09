# Cart Service

This is a simple Flask-based microservice for managing a user's shopping cart. It supports adding, removing, and viewing items in the cart.

## Installation

1.  Clone this repository:

    ```bash
    git clone https://github.com/Planteig1/cartService.git
    cd cart-service
    ```

2. Or use Docker

    docker run -it --rm -p 8080:80 cart-service



### Endpoints

- **Get all items in the cart**

    - **URL**: `/cart`
    - **Method**: `GET`
    - **Description**: Returns a list of all items currently in the cart.
    - **Response**:
        - `200 OK`: List of items.

- **Add an item to the cart**

    - **URL**: `/cart`
    - **Method**: `POST`
    - **Description**: Adds a product to the cart using a product ID. Data is fetched from the `dummyjson` service.
    - **Request Body**:

        ```json
        {
            "id": 1
        }
        ```

    - **Response**:
        - `201 Created`: Item added successfully.

- **Remove an item from the cart**

    - **URL**: `/cart`
    - **Method**: `DELETE`
    - **Description**: Removes an item from the cart using the product ID.
    - **Request Body**:

        ```json
        {
            "id": 1
        }
        ```

    - **Response**:
        - `201 Created`: Item deleted successfully.

