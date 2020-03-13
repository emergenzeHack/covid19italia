require 'nokogiri'
require 'rinku'

module Jekyll
  module AutoLinkFilter
    def auto_link(input)
      html = Nokogiri::HTML.fragment(Rinku.auto_link(input, :all, 'target="_blank"'))
      html.to_html
    end
  end
end

Liquid::Template.register_filter(Jekyll::AutoLinkFilter)
