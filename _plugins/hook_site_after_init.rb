require 'fileutils'

Jekyll::Hooks.register :site, :after_init do |site|
    FileUtils.rm_r '_data/', force: true
    system("git clone --depth 1 https://github.com/drizzt/covid19italia_opendata _data/")
end
