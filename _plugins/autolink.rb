require 'rinku'

module Jekyll
  module AutoLinkFilter
    def auto_link(input)
      Rinku.auto_link(input, :all, 'target="_blank"')
    end
  end
end

Liquid::Template.register_filter(Jekyll::AutoLinkFilter)
