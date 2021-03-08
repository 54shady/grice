#!/usr/bin/env sh

programs=(
"mpd"
"ncmpcpp"
"ranger"
"rofi"
"terminator"
"dunst"
"zathura"
"mpv"
"qutebrowser"
"sxhkd"
".toprc"
".bashrc"
".gitconfig"
".tmux.conf"
".xprofile"
".bash_profile"
".xinitrc"
".xsession"
".url_handler"
".extract_urlview"
".Xresources"
)

for d in ${programs[@]}
do
	DEFAULT_DIR="$HOME/.config/$d"
	# all the .XXX config file goes to the $HOME/
	if [ `echo $d | grep "^\."` ]
	then
		[ -f $HOME/$d ] && rm -rvf $HOME/$d
		ln -s $PWD/dotfile/dot_${d##.} $HOME/$d
	else # individual setup directory goes to the $HOME/.config/
		[ -d $DEFAULT_DIR ] && rm -rvf $DEFAULT_DIR
		ln -s $PWD/$d $HOME/.config/$d
	fi
done

# setup vim
[ -d $HOME/.vim ] && rm -rvf $HOME/.vim
[ -h $HOME/.vimrc -o -f $HOME/.vimrc ] && rm -rvf $HOME/.vimrc
ln -s $PWD/vim $HOME/.vim
ln -s $PWD/vim/vimrc $HOME/.vimrc
