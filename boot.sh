#Stop the background process
sudo hciconfig hci0 down
sudo systemctl daemon-reload
sudo /etc/init.d/bluetooth start
# Update  mac address
./updateMac.sh
#Update Name
./updateName.sh My_Mouse_Keyboard
#Get current Path
export C_PATH=$(pwd)
echo $C_PATH

tmux kill-window -t thanhle:app >/dev/null 2>&1

[ ! -z "$(tmux has-session -t thanhle 2>&1)" ] && tmux new-session -s thanhle -n app -d
[ ! -z "$(tmux has-session -t thanhle:app 2>&1)" ] && {
    tmux new-window -t thanhle -n app
}
[ ! -z "$(tmux has-session -t thanhle:app.1 2>&1)" ] && tmux split-window -t thanhle:app -h
[ ! -z "$(tmux has-session -t thanhle:app.2 2>&1)" ] && tmux split-window -t thanhle:app.1 -v
tmux send-keys -t thanhle:app.0 'cd $C_PATH/server && sudo python3 ./btk_server.py' C-m
tmux send-keys -t thanhle:app.1 'cd $C_PATH/mouse  && reset && cd ..' C-m
tmux send-keys -t thanhle:app.2 'cd $C_PATH/keyboard  && reset && cd ..' C-m
tmux send-keys -t thanhle:app.1 'bluetoothctl' C-m

# python3 find_directions.py
# scp out.txt rewq3@raspberrypi:/home/rewq3/Desktop/Projects/WordHuntBot
# ssh rewq3@raspberrypi "python3 /home/rewq3/Desktop/Projects/WordHuntBot/main.py"