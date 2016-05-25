# encoding: utf-8
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

module Azure::ARM::CDN
  module Models
    #
    # Model object.
    #
    class CustomDomainPropertiesParameters

      include MsRestAzure

      # @return [String] The host name of the custom domain. Must be a domain
      # name.
      attr_accessor :host_name

      #
      # Validate the object. Throws ValidationError if validation fails.
      #
      def validate
        fail MsRest::ValidationError, 'property host_name is nil' if @host_name.nil?
      end

      #
      # Serializes given Model object into Ruby Hash.
      # @param object Model object to serialize.
      # @return [Hash] Serialized object in form of Ruby Hash.
      #
      def self.serialize_object(object)
        object.validate
        output_object = {}

        serialized_property = object.host_name
        output_object['hostName'] = serialized_property unless serialized_property.nil?

        output_object
      end

      #
      # Deserializes given Ruby Hash into Model object.
      # @param object [Hash] Ruby Hash object to deserialize.
      # @return [CustomDomainPropertiesParameters] Deserialized object.
      #
      def self.deserialize_object(object)
        return if object.nil?
        output_object = CustomDomainPropertiesParameters.new

        deserialized_property = object['hostName']
        output_object.host_name = deserialized_property

        output_object
      end
    end
  end
end