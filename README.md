# Make things work first

## Step 1: Setup

```
 sudo ./setup.sh
```

Just do this step once

## Step 2: Run the Server

```
./boot.sh
```

then on the second tmux window, run

```
agent on
```

```
default-agent
```

```
discoverable on
```

http://web.archive.org/web/20210308091008/https://thanhle.me/make-raspberry-pi3-as-an-emulator-bluetooth-keyboard/ for more info

## Step 3: Run the Solver from your local pc

- make sure you have password-less access to your raspberry pi through public key authentication

```
./start.sh
```
