FROM httpd:bookworm

COPY /myapp /root/app
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN apt-get update && \
    apt-get install -y software-properties-common gnupg supervisor libharfbuzz-dev libfribidi-dev libssl-dev libcurl4-openssl-dev libxml2-dev libcairo2-dev libxt-dev xtail
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-key '95C0FAF38DB3CCAD0C080A7BDC78B2DDEABC47B7' && \
    add-apt-repository 'deb http://cloud.r-project.org/bin/linux/debian bookworm-cran40/' && \
    apt-get update
RUN apt-get install -y r-base

RUN R -e "install.packages(c('BiocManager', 'shiny', 'tidyr', 'dplyr', 'ggplot2', 'readr', 'magrittr', 'tibble', 'stringr'), repos='https://cran.rstudio.com/')" && \
    R -e "BiocManager::install(c('RCX', 'SummarizedExperiment'))"

EXPOSE 80 3838
CMD ["/usr/bin/supervisord"]
