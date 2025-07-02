from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import JSONSearchTool
from crewai_tools import CSVSearchTool
from crewai_tools import SerperDevTool
from crewai_tools import PDFSearchTool

@CrewBase
class RealestatepacketcrewAutomationProjectSetupGuideCrew():
    """RealestatepacketcrewAutomationProjectSetupGuide crew"""

    @agent
    def inputparser(self) -> Agent:
        return Agent(
            config=self.agents_config['inputparser'],
            tools=[JSONSearchTool(), CSVSearchTool()],
        )

    @agent
    def listingfetcher(self) -> Agent:
        return Agent(
            config=self.agents_config['listingfetcher'],
            tools=[SerperDevTool()],
        )

    @agent
    def listingorganizer(self) -> Agent:
        return Agent(
            config=self.agents_config['listingorganizer'],
            tools=[CSVSearchTool()],
        )

    @agent
    def scheduleoptimizer(self) -> Agent:
        return Agent(
            config=self.agents_config['scheduleoptimizer'],
            tools=[SerperDevTool()],
        )

    @agent
    def templateformatter(self) -> Agent:
        return Agent(
            config=self.agents_config['templateformatter'],
            tools=[PDFSearchTool()],
        )

    @agent
    def export(self) -> Agent:
        return Agent(
            config=self.agents_config['export'],
            tools=[],
        )


    @task
    def validate_and_normalize_inputs(self) -> Task:
        return Task(
            config=self.tasks_config['validate_and_normalize_inputs'],
            tools=[JSONSearchTool(), CSVSearchTool()],
        )

    @task
    def fetch_and_parse_listings(self) -> Task:
        return Task(
            config=self.tasks_config['fetch_and_parse_listings'],
            tools=[SerperDevTool()],
        )

    @task
    def annotate_and_rank_listings(self) -> Task:
        return Task(
            config=self.tasks_config['annotate_and_rank_listings'],
            tools=[CSVSearchTool()],
        )

    @task
    def build_showing_schedule(self) -> Task:
        return Task(
            config=self.tasks_config['build_showing_schedule'],
            tools=[SerperDevTool()],
        )

    @task
    def format_into_pdf(self) -> Task:
        return Task(
            config=self.tasks_config['format_into_pdf'],
            tools=[PDFSearchTool()],
        )

    @task
    def export_packet(self) -> Task:
        return Task(
            config=self.tasks_config['export_packet'],
            
        )


    @crew
    def crew(self) -> Crew:
        """Creates the RealestatepacketcrewAutomationProjectSetupGuide crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
