require 'fileutils'

Jekyll::Hooks.register :site, :after_init do |site|
    if site.config.include? 'dataurl'
        dataurl = site.config['dataurl']
        if (Dir.exists? '_data/machgen/.git') && (! ENV.include? 'NETLIFY')
            system("git -C _data/machgen/ pull --rebase --autostash #{dataurl}")
        else
            FileUtils.rm_r '_data/machgen/', force: true
            system("git clone --depth 1 #{dataurl} _data/machgen/")
        end
    end
end
