require 'fileutils'

Jekyll::Hooks.register :site, :after_init do |site|
    if site.config.include? 'dataurl'
        dataurl = site.config['dataurl']
        if (Dir.exists? '_data/.git') && (! ENV.include? 'NETLIFY')
            system("git -C _data pull --rebase --autostash #{dataurl}")
        else
            FileUtils.rm_r '_data/', force: true
            system("git clone --depth 1 #{dataurl} _data/")
        end
    end
end
