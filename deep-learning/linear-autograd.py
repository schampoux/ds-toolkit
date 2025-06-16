import torch
import torch.optim
import logging 

def model(t_u, w, b): 
    """
    Returns a tensor of predicted values using the inputs in a linear model. 
    t_u: Dependent variable. Input Tensor. Data we will use to predict the output t_c 
    w: Weight parameter. PyTorch scalar (zero-dimensional tensor)
    b: Bias parameter (Offset parameter). The bias is what the output would be if all the inputs were zero. 
    """
    return w * t_u + b

def loss_fn(t_p, t_c): 
    """
    Mean square loss function. 
    t_p: predicted value
    t_c: actual value
    """
    squared_diffs = (t_p-t_c)**2
    return squared_diffs.mean() 

def training_loop(n_epochs, learning_rate, params, t_u, t_c):
    for epoch in range(1, n_epochs + 1):

        # Zero the gradients, preventing accumulation
        if params.grad is not None: 
            params.grad.zero_()

        t_p=model(t_u, *params)
        loss = loss_fn(t_p, t_c)
        loss.backward() 

        # Perform optimization step, updating params
        with torch.no_grad():
            params -= learning_rate * params.grad

        # Log
        if epoch % 500 == 0: 
            print(f'Epoch {epoch}, Loss {float(loss)}')

    return params

def training_loop_sgd(n_epochs, optimizer, params, t_u, t_c):
    for epoch in range(1, n_epochs+1):
        t_p = model(t_u, *params)
        loss = loss_fn(t_p, t_c)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if epoch % 500 == 0: 
            print(f'Epoch {epoch}, Loss {float(loss)}')

    return params

def training_loop_v(n_epochs, optimizer, params, train_t_u, train_t_c, val_t_u, val_t_c,):
    for epoch in range(1, n_epochs+1):
        train_t_p = model(train_t_u, *params)
        train_loss = loss_fn(train_t_p, train_t_c)

        with torch.no_grad():
            # Compute validation set loss for monitoring during training
            val_t_p = model(val_t_u, *params)
            val_loss = loss_fn(val_t_p, val_t_c)

            # No need to build the autograd graph on val_loss
            assert val_loss.requires_grad == False 

        optimizer.zero_grad()
        train_loss.backward()
        optimizer.step()

        if epoch <=3 or epoch % 500 == 0:
            print(f'Epoch {epoch}, Training Loss {round(float(train_loss),4)}, \n\tValidation Loss {round(float(val_loss),4)}')

    return params
    
def shuffle_indices(t_u, t_c)-> tuple[torch.tensor]:
    n_samples = t_u.shape[0]
    n_val = int(0.2 * n_samples) 

    shuffled_indices = torch.randperm(n_samples)
    train_indices = torch.randperm(n_samples) 

    train_indices = shuffled_indices[:-n_val]
    val_indices = shuffled_indices[-n_val:]

    train_t_u = t_u[train_indices]
    train_t_c = t_c[train_indices]

    val_t_u = t_u[val_indices]
    val_t_c = t_c[val_indices]

    return train_t_u, train_t_c, val_t_u, val_t_c

def main(): 
    t_c = torch.tensor([0.5, 14.0, 15.0, 28.0, 11.0, 8.0, 3.0, -4.0, 6.0, 13.0, 21.0])
    t_u = torch.tensor([35.7, 55.9, 58.2, 81.9, 56.3, 48.9, 33.9, 21.8, 48.4, 60.4, 68.4])

    # Normalize
    t_un = t_u*.1

    
    # params = training_loop(
    #     n_epochs = 5000,
    #     learning_rate = 1e-2,
    #     params = torch.tensor([1.0,0.0], requires_grad=True),
    #     t_u = t_un,
    #     t_c = t_c
    # )


    # # SGD Optimizer

    # params = torch.tensor([1.0,0.0], requires_grad=True)
    # learning_rate = 1e-2
    # optimizer = torch.optim.SGD([params], lr=learning_rate)
    # trained_params = training_loop_sgd(
    #     n_epochs = 5000,
    #     optimizer = optimizer,
    #     params = params,
    #     t_u = t_un,
    #     t_c = t_c
    # )
    # print(trained_params)

    # Validation set 
    params = torch.tensor([1.0,0.0], requires_grad=True)
    learning_rate = 1e-2
    optimizer = torch.optim.SGD([params], lr=learning_rate)
    train_t_u, train_t_c, val_t_u, val_t_c = shuffle_indices(t_u, t_c)

    # Normalize
    train_t_un = 0.1 * train_t_u
    val_t_un = 0.1 * val_t_u

    trained_params = training_loop_v(
        n_epochs = 5000,
        optimizer = optimizer,
        params = params,
        train_t_u = train_t_un,
        train_t_c = train_t_c, 
        val_t_u = val_t_un, 
        val_t_c = val_t_c,
    )
    print(trained_params)

if __name__ =="__main__":
    main() 