library(shiny)
library(tidyverse)
library(ggplot2)
library(plotly)

data <- read.csv("cricket_data.csv")

ui <- fluidPage(
    titlePanel("ICC Batsman Dashboard (1999–2019)"),

    sidebarLayout(
        sidebarPanel(
            selectInput("country", "Select Country:",
                        choices = c("All", unique(data$Country)),
                        selected = "All"),

            sliderInput("year", "Select Year Range:",
                        min = min(data$Year),
                        max = max(data$Year),
                        value = c(min(data$Year), max(data$Year)),
                        sep = "")
        ),

        mainPanel(
            fluidRow(
                column(6, h3("Total Runs"),
                       textOutput("totalRuns")),
                column(6, h3("Total Balls Faced"),
                       textOutput("totalBalls"))
            ),
            hr(),

            fluidRow(
                column(6, plotOutput("resultPie")),
                column(6, tableOutput("topBatsman"))
            ),
            hr(),

            h3("Total Runs by Batsman"),
            plotOutput("runBar"),

            hr(),
            h3("Country-wise Summary"),
            tableOutput("countrySummary")
        )
    )
)

server <- function(input, output) {

    filtered <- reactive({
        df <- data
        if (input$country != "All") {
            df <- df %>% filter(Country == input$country)
        }
        df <- df %>% filter(Year >= input$year[1], Year <= input$year[2])
        return(df)
    })

    output$totalRuns <- renderText({
        sum(filtered()$Runs, na.rm = TRUE)
    })

    output$totalBalls <- renderText({
        sum(filtered()$Balls, na.rm = TRUE)
    })

    output$resultPie <- renderPlot({
        filtered() %>%
            count(Result) %>%
            ggplot(aes(x = "", y = n, fill = Result)) +
            geom_col(width = 1) +
            coord_polar(theta = "y") +
            theme_void() +
            ggtitle("Match Result Distribution")
    })

    output$topBatsman <- renderTable({
        filtered() %>%
            group_by(Player) %>%
            summarise(
                `4s` = sum(4s),
                `6s` = sum(6s),
                Runs = sum(Runs)
            ) %>%
            arrange(desc(Runs)) %>%
            head(10)
    })

    output$runBar <- renderPlot({
        filtered() %>%
            group_by(Player) %>%
            summarise(Runs = sum(Runs)) %>%
            arrange(desc(Runs)) %>%
            ggplot(aes(x = reorder(Player, Runs), y = Runs, fill = Runs)) +
            geom_bar(stat = "identity") +
            coord_flip() +
            theme_minimal() +
            ggtitle("Top Batsman by Total Runs")
    })

    output$countrySummary <- renderTable({
        filtered() %>%
            group_by(Country, Result) %>%
            summarise(Matches = n()) %>%
            pivot_wider(names_from = Result, values_from = Matches, values_fill = 0)
    })

}

shinyApp(ui = ui, server = server)
