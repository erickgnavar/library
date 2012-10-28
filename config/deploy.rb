set :application, "library"
set :repository,  "erickxls@github.com:library/library.git"
set :deploy_to, "/home/ubuntu/www/#{application}"
set :user, "ubuntu"
set :branch, "master"
set :port, 6969

set :scm, :git
# Or: `accurev`, `bzr`, `cvs`, `darcs`, `git`, `mercurial`, `perforce`, `subversion` or `none`

role :web, "23.23.150.127"                          # Your HTTP server, Apache/etc
role :app, "your app-server here"                          # This may be the same as your `Web` server
role :db,  "your primary db-server here", :primary => true # This is where Rails migrations will run
role :db,  "your slave db-server here"

# if you want to clean up old releases on each deploy uncomment this:
# after "deploy:restart", "deploy:cleanup"

# if you're still using the script/reaper helper you will need
# these http://github.com/rails/irs_process_scripts

# If you are using Passenger mod_rails uncomment this:
namespace :deploy do
	task :start do ; end
	task :stop do ; end
	task :restart, :roles => :app, :except => { :no_release => true } do
	run "#{try_sudo} touch #{File.join(current_path,'tmp','restart.txt')}"
	end
end