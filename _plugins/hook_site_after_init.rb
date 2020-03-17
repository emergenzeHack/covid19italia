require 'fileutils'

Jekyll::Hooks.register :site, :after_init do |site|
    FileUtils.rm_r '_data/', force: true
    system("git clone --depth 1 https://github.com/emergenzeHack/covid19italia_data _data/")
end
